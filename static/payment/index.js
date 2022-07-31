var stripe = Stripe(STRIPE_PUBLISHABLE_KEY);

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();

var card = elements.create("card");
card.mount("#card-element");

card.on('change', function(event) {
    var displayError = document.getElementById('card-errors')
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    } else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    var custName = document.getElementById('fullName').value;
    var custAdd = document.getElementById('address').value;
    var custAdd2 = document.getElementById('address2').value;
    var zipCode = document.getElementById('zip').value;

    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/orders/add/',
        data: {
            order_key: clientsecret,
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: "post",
        },
        success: function (json) {
            console.log(json.success)

            stripe.confirmCardPayment(clientsecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        address: {
                            line1:custAdd,
                            line2:custAdd2,
                        },
                        name: custName
                    },
                }
            }).then(function(result) {
                if (result.error) {
                    console.log('payment ettot')
                    console.log(result.error.message);
                } else {
                    if (result.paymentIntent.status === 'succeeded') {
                        console.log('payment processed')
                        window.location.replace("http://127.0.0.1:8000/payment/orderplaced");
                    }
                }
            });
        },
        error: function(xhr, errmsg, err) {},
    });
});