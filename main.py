import requests

# GitHub Tokenいれて(必要な権限はrepo管理のみ)
GITHUB_TOKEN = "ghp_から始まるやつね"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

user_response = requests.get("https://api.github.com/user", headers=headers)
user_response.raise_for_status()
username = user_response.json()["login"]

# 自分が所有しているすべてのリポジトリを取得
repos_url = "https://api.github.com/user/repos?per_page=100&type=owner"
repos_response = requests.get(repos_url, headers=headers)
repos_response.raise_for_status()
repos = repos_response.json()

for repo in repos:
    if not repo["private"]: 
# ちなみに全部publicにしたいときは
# if repo ["private"] 
# にすれば動くよ
        aaa = repo["name"]
        print(f"{aaa}処理中")
        patch_url = f"https://api.github.com/repos/{username}/{aaa}"
        patch_response = requests.patch(patch_url, headers=headers, json={"private": True}) 
# publicにするときは
# json={"private": False}に
        if patch_response.status_code == 200:
            print(f"{aaa}は成功")
        else:
            print(f"{aaa}は失敗: {patch_response.status_code} {patch_response.text}")
