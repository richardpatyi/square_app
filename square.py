"""A simple Flask app to square a number."""

from flask import Flask, request, render_template_string

app = Flask(__name__)

def square_number(number: float) -> float:
    """Returns the square of the given number."""
    return number ** 2

HTML_TEMPLATE = """
<form method="POST">
  Number: <input name="number" type="number" step="any">
  <input type="submit" value="Calculate">
</form>
{% if result is not none %}
  <p>Result: {{ result }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles form input and displays the squared result."""
    result = None
    if request.method == "POST":
        try:
            number = float(request.form["number"])
            result = square_number(number)
        except ValueError:
            result = "Invalid input!"
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == "__main__":
    app.run(debug=True)
