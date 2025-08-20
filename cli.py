import argparse
import pandas as pd
from preprocessor import DataPreprocessing


def main():

    parser = argparse.ArgumentParser(description="Data Preprocessing CLI Tool")

    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the input dataset file (CSV or Excel)",
    )
    parser.add_argument(
        "--target",
        type=str,
        required=True,
        help="Name of the target column",
    )
    parser.add_argument(
        "--scaling",
        type=str,
        choices=["standard", "minmax"],
        default="standard",
        help="Scaling method: 'standard' or 'minmax' (default: standard)",
    )
    parser.add_argument(
        "--test_size",
        type=float,
        default=0.2,
        help="Proportion of test data (default: 0.2)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="processed_output.csv",
        help="Path to save processed dataset (CSV or Excel based on extension)",
    )

    args = parser.parse_args()


    print("\n🔶 Initial Dataset Preview:")
    if args.file.endswith(".csv"):
        df_preview = pd.read_csv(args.file)
    elif args.file.endswith(".xlsx"):
        df_preview = pd.read_excel(args.file)
    else:
        raise ValueError("Unsupported file format. Please provide CSV or Excel.")
    print(df_preview.head(), "\n")

    preprocessor = DataPreprocessing(
        filepath=args.file,
        target_column=args.target,
        scaling=args.scaling,
        test_size=args.test_size,
        config=None,
    )

    df = preprocessor.load_data()
    df = preprocessor.handle_missing_values()
    df = preprocessor.encode_categorical()
    df = preprocessor.scaling_feature(method=args.scaling)
    X_train, X_test, y_train, y_test = preprocessor.split_data(
    target_column=args.target,
    test_size=args.test_size
)

    print("\n\n✅ Data Cleaning Summary Report:")
    for key, value in preprocessor.report.items():
        print(f"\n🔹 {key}:")
        print(value)

    print("\n📊 Final Processed DataFrame:")
    print(df.head())

    if args.output.endswith(".csv"):
        df.to_csv(args.output, index=False)
    elif args.output.endswith(".xlsx"):
        df.to_excel(args.output, index=False)
    else:
        raise ValueError("Unsupported output format. Please use .csv or .xlsx")

    print(f"\n💾 Processed dataset saved as: {args.output}")


if __name__ == "__main__":
    main()
