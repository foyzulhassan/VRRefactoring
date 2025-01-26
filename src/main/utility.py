#utility package

def extract_details(result):
    strip_repo_link = result.split('/')
    owner_name = strip_repo_link[3]
    proj = strip_repo_link[4].split('.git')
    project_name = proj[0]
    return owner_name,project_name

def repo_collection(path,repo):
    with open(path,'r') as file:
        res = file.read().strip()
        final_res = res.split("\n")
    return final_res