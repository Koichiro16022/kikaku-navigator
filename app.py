from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# デモ用の固定データ（8265と入力された際の挙動を定義）
DEMO_DATA = {
    "8265": {
        "target": "JIS B 8265",
        "name": "圧力容器の構造",
        "latest_year": "2024",
        "local_year": "2010",
        "has_pdf": False
    },
    "8266": {
        "target": "JIS B 8266",
        "name": "圧力容器の構造―特定規格",
        "latest_year": "2022",
        "local_year": "2022",
        "has_pdf": True
    }
}

@app.route('/')
def index():
    # templates/index.html を読み込みます
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    # 入力された文字が含まれる候補を抽出
    results = [v for k, v in DEMO_DATA.items() if query in k or query in v['target']]
    return jsonify(results)

if __name__ == '__main__':
    # ポート5001で起動します（ブラウザでは http://127.0.0.1:5001 でアクセス）
    app.run(debug=True, port=5001)