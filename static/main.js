console.log("Sanity check!");

// Get Stripe publishable key
fetch("/payment/config/")
  .then((result) => { return result.json(); })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey, {
      stripeAccount: 'acct_1JWXT2Fay7qbEsC6'
    });

    // Event handler
    document.querySelector("#submitBtn").addEventListener("click", () => {
      // Current Campaign ID
      var segment_str = window.location.pathname;
      var segment_array = segment_str.split('/');
      var last_segment = segment_array.pop();
      console.log(last_segment)

      var ele = document.getElementById('detail-amount').innerHTML;
      console.log('amount', ele.slice(1));
      var real_amount = ele.slice(1);
      var amount = parseInt(real_amount) * 100;
      const req_data = { amount: amount };

      // Get Checkout Session ID
      fetch(`/payment/create-checkout-session/?param1=${encodeURIComponent(req_data.amount)}&param2=${encodeURIComponent(last_segment)}`, {
        method: 'GET',
      })
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log('data', data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.sessionId })
        })
        .then((res) => {
          console.log(res);
        });
    });

    document.querySelector("#submitBtn1").addEventListener("click", () => {
      // Current Campaign ID
      var segment_str = window.location.pathname;
      var segment_array = segment_str.split('/');
      var last_segment = segment_array.pop();
      console.log(last_segment)

      var ele = document.getElementById('detail-amount').innerHTML;
      console.log('amount', ele.slice(1));
      var real_amount = ele.slice(1);
      var amount = parseInt(real_amount) * 100;
      const req_data = { amount: amount };

      // Get Checkout Session ID
      fetch(`/payment/create-checkout-session/?param1=${encodeURIComponent(req_data.amount)}&param2=${encodeURIComponent(last_segment)}`, {
        method: 'GET',
      })
        .then((result) => { return result.json(); })
        .then((data) => {
          console.log('data', data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.sessionId })
        })
        .then((res) => {
          console.log(res);
        });
    });
  });