from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form method="post" action="/multiply">
            Matrix A (e.g., 1,2;3,4): <input name="matrix_a"><br>
            Matrix B (e.g., 5,6;7,8): <input name="matrix_b"><br>
            <input type="submit" value="Multiply">
        </form>
    '''

@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        a_str = request.form['matrix_a']
        b_str = request.form['matrix_b']
        
        A = [[int(num) for num in row.split(',')] for row in a_str.strip().split(';')]
        B = [[int(num) for num in row.split(',')] for row in b_str.strip().split(';')]
        
        result = []
        for i in range(len(A)):
            row = []
            for j in range(len(B[0])):
                cell = sum(A[i][k] * B[k][j] for k in range(len(B)))
                row.append(cell)
            result.append(row)
        
        return f"<h3>Result:</h3> {result}"
    
    except Exception as e:
        return f"Error: {e}"

# ✅ ADD THIS BELOW LINE
if __name__ == '__main__':
    app.run(debug=True)
