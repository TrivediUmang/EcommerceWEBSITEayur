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