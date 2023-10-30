function submitForm(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    fetch('/predict/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predicted-quality').innerText = parseFloat(data.quality).toFixed(2);
    });
}

function fetchRandomData() {
    fetch('/random_data/')
    .then(response => response.json())
    .then(data => {
        document.querySelector("[name='fixed_acidity']").value = data["fixed acidity"];
        document.querySelector("[name='volatile_acidity']").value = data["volatile acidity"];
        document.querySelector("[name='residual_sugar']").value = data["residual sugar"];
        document.querySelector("[name='free_sulfur_dioxide']").value = data["free sulfur dioxide"];
        document.querySelector("[name='density']").value = data["density"];
        document.querySelector("[name='pH']").value = data["pH"];
        document.querySelector("[name='sulphates']").value = data["sulphates"];
        document.querySelector("[name='alcohol']").value = data["alcohol"];
    });
    // 防止表單提交後的頁面刷新
    return false;
}
