from preprocessor import DataPreprocessing
import pandas as pd

def main():
    file_path = "Employee.csv"
    target_col = "LeaveOrNot"

    df_print = pd.read_csv(file_path)
    
    
    print("\n🔶Initial Dataset")
    print(df_print.head())
    print("\n")

    preprocessor = DataPreprocessing(
        filepath=file_path,
        target_column=target_col,
        scaling="standard",
        test_size=0.2,
        config=None,
    )

    df = preprocessor.load_data()    
    df = preprocessor.handle_missing_values()
    df = preprocessor.encode_categorical()
    df = preprocessor.scaling_feature(method="standard")

    X_train, X_test, y_train, y_test = preprocessor.split_data(
        target_column=target_col
    )

    print("\n\n✅ Data Cleaning Summary Report:")
    for key, value in preprocessor.report.items():
        print(f"\n🔹 {key}:")
        print(value)

    print("\n\n📊 Final Processed DataFrame:")
    print(df.head())

if __name__ == "__main__":
    main()
