import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['Name'].tolist())

    Name                       = df['Name'].tolist()

    Worth                      = df['Worth'].tolist()

    # print(df['quebec'].tolist())

    result_dict = {
        'Name'                        : Name,
        'Worth '                      :Worth
    }

    print(result_dict)

    return result_dict

def add_row(Name, Worth):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'Name'                   : Name, 
        'Worth'                  : Worth
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()