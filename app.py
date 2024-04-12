from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from collections import defaultdict
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return 'Server started'

@app.route('/post', methods=['POST'])
def handle_post():
    # Ensure there is data in the request

    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    html_doc = data["html"]

    soup = BeautifulSoup(html_doc, 'html.parser')

    class_elements = defaultdict(list)

    # 모든 태그를 찾아서 클래스 이름을 그에 해당하는 요소 리스트에 추가
    for tag in soup.find_all(True):
        class_names = tag.get('class', [])
        for class_name in class_names:
            class_elements[class_name].append(tag.get_text(strip=True))

    # 각 클래스 이름에 해당하는 리스트의 길이를 맞추기 위해 빈 문자열로 채움
    max_length = max(len(elements) for elements in class_elements.values())
    for elements in class_elements.values():
        elements.extend([''] * (max_length - len(elements)))

    # pandas DataFrame 생성
    df = pd.DataFrame(class_elements)

    # CSV 파일로 저장
    # df.to_csv('class_elements.csv', index=False, encoding='utf-8-sig')
    # print("CSV 파일이 성공적으로 생성되었습니다.")





   # Convert DataFrame to JSON
    result_json = df.to_json(orient='records')
    return jsonify({"data": result_json})

if __name__ == '__main__':
    app.run('0.0.0.0', port=8090, debug=True)



# html_doc = ""

# soup = BeautifulSoup(html_doc, 'html.parser')

# class_elements = defaultdict(list)

# # 모든 태그를 찾아서 클래스 이름을 그에 해당하는 요소 리스트에 추가
# for tag in soup.find_all(True):
#     class_names = tag.get('class', [])
#     for class_name in class_names:
#         class_elements[class_name].append(tag.get_text(strip=True))

# # 각 클래스 이름에 해당하는 리스트의 길이를 맞추기 위해 빈 문자열로 채움
# max_length = max(len(elements) for elements in class_elements.values())
# for elements in class_elements.values():
#     elements.extend([''] * (max_length - len(elements)))

# # pandas DataFrame 생성
# df = pd.DataFrame(class_elements)

# # CSV 파일로 저장
# df.to_csv('class_elements.csv', index=False, encoding='utf-8-sig')
# print("CSV 파일이 성공적으로 생성되었습니다.")
