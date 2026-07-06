import json

file_path = "mian.ipynb"
with open(file_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    if cell["cell_type"] == "code":
        source = "".join(cell["source"])
        if "tree.plot_tree" in source:
            cell["source"] = [
                "# 그림(시각화) 크기 설정\n",
                "plt.figure(figsize=(16, 12))\n",
                "\n",
                "# 학생들이 쉽게 이해할 수 있도록 안내 문구 추가\n",
                "plt.title('AI의 판단 기준 (왼쪽 화살표 = True(예) / 오른쪽 화살표 = False(아니오))', fontsize=18, pad=20)\n",
                "\n",
                "# AI가 생각한 기준을 트리 그림으로 나타내기\n",
                "tree.plot_tree(ai_model, \n",
                "               feature_names=['꽃받침 길이', '꽃받침 너비', '꽃잎 길이', '꽃잎 너비'],  \n",
                "               class_names=ai_model.classes_,\n",
                "               filled=True,      # 박스에 색상 채우기\n",
                "               fontsize=12,      # 글자 크기 키우기 (True/False가 잘 보이도록)\n",
                "               rounded=True)     # 박스 모서리 둥글게\n",
                "\n",
                "# 완성된 그림을 파일로 저장하기\n",
                "plt.savefig('분석결과_트리.png', dpi=300, bbox_inches='tight')\n",
                "\n",
                "# 그림 화면에 보여주기\n",
                "plt.show()"
            ]

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook updated to make True/False more visible.")
