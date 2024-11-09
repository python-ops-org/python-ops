import pandas as pd

def write(filename, names, scores):
    try:
        df = pd.DataFrame({'name': names, 'score': scores})
        df.to_csv(filename, index=False)
        print(f"Data written to {filename}")
    except Exception as e:   
        print(f"Error: {e}")

def parse(filename):
    try:
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            print(f"name: {row['name']}, score: {row['score']}")
    except Exception as e:
        print(f"Error: {e}")        

if __name__ == "__main__":
    filename = "out.csv"
    names = ["sachin","rahul","virat"]
    scores = ["101", "102", "103"]
    write(filename, names, scores)
    parse(filename)
