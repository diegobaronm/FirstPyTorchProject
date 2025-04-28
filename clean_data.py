import polars as pl
import matplotlib.pyplot as plt
import os

# Function to clean the job description text
def clean_job_description(dataset):
    
    # Remove the following characters
    unwanted_chars = ['\n', '\n\n', '\n\n\n' , '\n\n\n\n','\r', '\t', '*', '  ', '   ']
    mapping = {}
    for char in unwanted_chars:
        mapping[char] = ''
    mapping['**'] = ' '
    
    dataset = dataset.with_columns(cleaned_description=pl.col('description').str.replace_many(mapping))

    return dataset

def load_data(file_path):
    """Load data from an Excel file using Polars."""
    dataset = pl.read_excel(file_path, sheet_name='Sheet1')

    # Do all the preprocessing here:
    # Chop the first 3 columns
    dataset = dataset[:, 3:]

    # Only select the following columns
    columns_to_select = ['site', 'title', 'company', 'location', 'job_type', 'date_posted', 'salary_source',
                         'interval', 'min_amount', 'max_amount', 'currency', 'is_remote', 'job_level',
                         'job_function', 'company_industry', 'listing_type', 'description','company_num_employees',
                         'company_revenue', 'company_description', 'mean_salary']

    result = dataset.select(pl.col(columns_to_select))

    result = clean_job_description(result)

    return result


def print_example(dataset, index):
    """Print an example row from the dataset."""
    if index < len(dataset):
        # Print every column and the corresponding value. Print raw value
        for column in dataset.columns:
            print(f"{column}: {dataset[index, column]}")
        
    else:
        print(f"Index {index} is out of bounds for the dataset with length {len(dataset)}.")

def show_statistics(data, file_name):
    """Display basic statistics of the dataset."""
    print(f"Statistics for {file_name}:")
    print(data.describe())

    # Print shape
    print(f"Shape: {data.shape}")

    for column, col_type in zip(data.columns, data.dtypes):
        print(f"Column: {column}, Type: {col_type}")

    # Print the 1000th row
    print_example(data, 1000)

def save_data(data, file_name):
    ''' Save to a CSV file '''
    data.write_csv(file_name)

def main():
    data_folder = "data"
    file_name = 'all_jobs.xlsx'
    file_path = os.path.join(data_folder, file_name)
    data = load_data(file_path)
    show_statistics(data, file_name)

    save_data(data, os.path.join(data_folder, 'all_jobs_cleaned.csv'))

if __name__ == "__main__":
    main()