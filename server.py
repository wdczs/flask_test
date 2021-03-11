from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/obj_seg/<input_path>/<output_path>', methods=['POST'])
def obj_seg(input_path, output_path):
    res = dict(input_path=input_path, output_path=output_path, status=200)
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=8099)

