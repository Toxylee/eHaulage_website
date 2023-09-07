function pick_up() {
    const pick = document.getElementById("pick_psng").value;
    const dest = document.getElementById("dest_psng").value;
    fetch(`http://localhost:5000/new_order/${pick}/${dest}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("confirm").innerHTML = `
            Your order has been booked, your destination is ${data}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
