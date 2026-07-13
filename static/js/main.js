const faqs = document.querySelectorAll(".faq");

faqs.forEach(faq=>{

    faq.querySelector(".faq-question").addEventListener("click",()=>{

        faqs.forEach(item=>{

            if(item!==faq){

                item.classList.remove("active");

            }

        });

        faq.classList.toggle("active");

    });

});

// ===========================
// Product Quantity
// ===========================

const qtyInput = document.querySelector(".quantity input");

if (qtyInput) {

    const buttons = document.querySelectorAll(".quantity button");

    buttons[0].onclick = function () {

        let qty = parseInt(qtyInput.value);

        if (qty > 1) {
            qty--;
            qtyInput.value = qty;
        }

    };

    buttons[1].onclick = function () {

        let qty = parseInt(qtyInput.value);

        qty++;

        qtyInput.value = qty;

    };

}

// ===========================
// Product Image Change
// ===========================

function changeImage(image){

    const main = document.getElementById("mainProductImage");

    if(main){

        main.src = image.src;

    }

}