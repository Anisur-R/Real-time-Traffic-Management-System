from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# প্রাথমিক সিগন্যাল স্টেট
# ০: উত্তর-দক্ষিণ সবুজ, ১: পূর্ব-পশ্চিম সবুজ
traffic_state = {
    "current_light": "North-South",
    "color": "Green",
    "timer": 10
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    # এখানে লজিক থাকতে পারে যা সময়ের সাথে স্টেট পরিবর্তন করবে
    # তবে সিম্পল রাখার জন্য আমরা ফ্রন্টএন্ডে জাভাস্ক্রিপ্ট দিয়ে টাইমার কন্ট্রোল করব
    return jsonify(traffic_state)

if __name__ == '__main__':
    app.run(debug=True)