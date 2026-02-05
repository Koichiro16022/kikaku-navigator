from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# デモ用の固定データ
# has_pdf が True ならPDF表示、False なら未保有警告を出します
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
    # Codespaces環境で外部からアクセス可能にするため 0.0.0.0 で起動
    # ポートは先ほど確認した 5001 を使用します
    app.run(host='0.0.0.0', port=5001, debug=True)
