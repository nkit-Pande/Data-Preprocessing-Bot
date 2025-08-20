
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from logger import get_logger

logging = get_logger(__name__)


class DataPreprocessing:
    """
    A class for preprocessing datasets:
    - Load CSV/Excel files
    - Handle missing values
    - Encode categorical features
    - Scale numeric features
    - Split into train/test sets
    - Maintain a preprocessing report
    """

    def __init__(
        self, filepath, target_column=None, scaling=None, test_size=0.2, config=None
    ):
        """
        Initialize preprocessing object.

        Args:
            filepath (str): Path to the dataset (.csv or .xlsx).
            target_column (str): Column name for the target variable.
            scaling (str): Scaling method ("standard" or "minmax").
            test_size (float): Proportion of test data.
            config (dict): Optional configuration dictionary.
        """
        self.filepath = filepath
        self.target_column = target_column
        self.scaling = scaling
        self.test_size = test_size
        self.config = config

        self.df = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

        self.report = {
            "missing_values": {},
            "encodings": {},
            "scaling": None,
            "train_test_split": {},
        }

    def load_data(self):
        """
        Load dataset from CSV or Excel.
        Returns:
            pd.DataFrame: Loaded dataframe.
        """
        if self.filepath.endswith(".csv"):
            self.df = pd.read_csv(self.filepath)
        elif self.filepath.endswith(".xlsx"):
            self.df = pd.read_excel(self.filepath)
        else:
            raise ValueError(
                "Unsupported file format. Only CSV and Excel files are supported."
            )

        logging.info(f"Dataset loaded with shape {self.df.shape}")
        return self.df

    def handle_missing_values(self):
        """
        Handle missing values:
        - Numeric columns → fill with mean
        - Categorical columns → fill with mode
        Updates self.report['missing_values'].
        """
        missing_report = {}

        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if self.df[col].dtype in ["int64", "float64"]:
                    fill_value = self.df[col].mean()
                    # ✅ Fix: assign back instead of inplace=True
                    self.df[col] = self.df[col].fillna(fill_value)
                    missing_report[col] = f"Filled with Mean ({fill_value:.2f})"
                else:
                    fill_value = self.df[col].mode()[0]
                    # ✅ Fix: assign back instead of inplace=True
                    self.df[col] = self.df[col].fillna(fill_value)
                    missing_report[col] = f"Filled with Mode ({fill_value})"

        self.report["missing_values"] = missing_report
        logging.info(f"Missing values handled: {missing_report}")
        return self.df

    def encode_categorical(self):
        """
        Encode categorical columns:
        - Label Encoding if binary
        - One-Hot Encoding if multi-class
        Updates self.report['encodings'].
        """
        encoding = {}
        label_encoder = LabelEncoder()

        for col in self.df.select_dtypes(include=["object"]).columns:
            if self.df[col].nunique() == 2:
                self.df[col] = label_encoder.fit_transform(self.df[col])
                encoding[col] = "Label Encoding"
            else:
                dummies = pd.get_dummies(self.df[col], prefix=col)
                self.df = pd.concat([self.df.drop(columns=[col]), dummies], axis=1)
                encoding[col] = "One-Hot Encoding"

        self.report["encodings"] = encoding
        logging.info(f"Categorical columns encoded: {encoding}")
        return self.df

    def scaling_feature(self, method="standard"):
        """
        Scale numeric features:
        - 'standard' → Z-score Standardization
        - 'minmax' → Min-Max Scaling
        Updates self.report['scaling'].
        """
        scaling_method = {}
        numeric_cols = self.df.select_dtypes(include=["int64", "float64"]).columns

        if method == "standard":
            scaler = StandardScaler()
            self.df[numeric_cols] = scaler.fit_transform(self.df[numeric_cols])
            scaling_method["method"] = "Standardization (Z-score)"
        elif method == "minmax":
            scaler = MinMaxScaler()
            self.df[numeric_cols] = scaler.fit_transform(self.df[numeric_cols])
            scaling_method["method"] = "Min-Max Scaling"
        else:
            raise ValueError("Invalid scaling method. Choose 'standard' or 'minmax'.")

        self.report["scaling"] = scaling_method
        logging.info(f"Data scaled using {scaling_method}")
        return self.df

    def split_data(self, target_column, test_size=0.2, random_state=42):
        """
        Split dataset into train and test sets.
        Args:
            target_column (str): Target column name.
            test_size (float): Proportion of test set.
            random_state (int): Random seed.
        Returns:
            tuple: X_train, X_test, y_train, y_test
        """
        if target_column not in self.df.columns:
            raise ValueError(
                f"Target column '{target_column}' not found in the dataset."
            )

        X = self.df.drop(columns=target_column)
        y = self.df[target_column]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        self.report["train_test_split"] = {
            "target": target_column,
            "train_size": 1 - test_size,
            "test_size": test_size,
        }

        logging.info(
            f"Data split into training and testing sets with test size = {test_size}"
        )
        return self.X_train, self.X_test, self.y_train, self.y_test
