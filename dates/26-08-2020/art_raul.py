import requests

TOKEN = "b6aCCurUXr6nAAb2JtPaxV3KvK1Lct"
HEADERS = {"Content-Type": "application/json", "Authorization": f"Bearer {TOKEN}"}


def get_job_ids():
    nex = "/api/v2/jobs/"
    url = "http://192.168.56.159"

    results = []

    while True:
        response = requests.get(url + nex, headers=HEADERS)
        data = response.json()
        results += data["results"]

        if str(data["next"]) == "None":
            break
        else:
            nex = data["next"]

    return list(set([result["id"] for result in results]))

def get_file_name(job_id):
    #print(f"Fetching job id {job_id}")
    url = f"http://192.168.56.159/api/v2/jobs/{job_id}/stdout/?format=json"

    try:
        response_job = requests.get(url, headers=HEADERS)
        content = response_job.json()["content"]

        index = content.index("\"dest\"")
        start = content.index("\"", index + 6) + 1
        end = content.index("\"", start)

        path = content[start:end]
        file_name = path.split("/")[-1]
        if file_name == "":
            raise Exception("File name empty!")
        return file_name
    except:
        return "Not Present"

def main():
    job_ids = get_job_ids()
    file_names = list(map(get_file_name, job_ids))
    for i in range(len(file_names)):
        print(f"{job_ids[i]} {file_names[i]}")

if __name__ == "__main__":
    main()
