/**
 * Dashboard Main Slider
 */
window.addEventListener("DOMContentLoaded", (event) => {
    const sliderDashMainSecondary = document.querySelector(
        "#sliderDashMainSecondary"
    );
    const sliderDashMainPrimary = document.querySelector(
        "#sliderDashMainPrimary"
    );

    if (sliderDashMainSecondary && sliderDashMainPrimary) {
        /**
         * Secondary Slider
         */
        const secondarySlider = new Splide("#sliderDashMainSecondary", {
            // type: "loop",
            fixedWidth: 300,
            height: 230,
            gap: 30,
            cover: true,
            pagination: false,
            lazyLoad: true,
            autoplay: true,
            perPage: 1,
            perMove: 1,
            arrows: false,
            rewind: true,
            breakpoints: {
                991: {
                    fixedWidth: 260,
                    height: 187,
                },
            },
        }).mount();

        /**
         * Primary Slider
         */
        const primarySlider = new Splide("#sliderDashMainPrimary", {
            fixedWidth: 620,
            height: 300,
            type: "fade",
            heightRatio: 0.5,
            pagination: false,
            autoplay: true,
            arrows: false,
            cover: true,
            lazyLoad: true,
            rewind: true,
            breakpoints: {
                1200: {
                    fixedWidth: 400,
                },
            },
        }).mount();

        /**
         * Sliders Synchronization
         */
        primarySlider.sync(secondarySlider).mount();
        secondarySlider.on("moved dragged", function (index) {
            primarySlider.go(secondarySlider.index);
        });

        /**
         * Navigation
         */

        const nav = document.querySelector(".dash-main-slider__nav");
        const cat_card_count = $("#sliderDash-list li").length;
        if (nav && cat_card_count > 0) {
            const btnNext = nav.querySelector(".splide__arrow--next");
            const btnPrev = nav.querySelector(".splide__arrow--prev");

            if (btnNext && btnPrev) {
                btnNext.addEventListener("click", (e) => {
                    secondarySlider.go(">");
                });
                btnPrev.addEventListener("click", (e) => {
                    secondarySlider.go("<");
                });
            }
        }
    }
});

/**
 * Dashboard Slider
 */

window.addEventListener("DOMContentLoaded", (event) => {
    /**
     * Typical Slider for Dashboard
     */
    const sliderDash = document.querySelectorAll("#sliderDash");
    if (sliderDash) {
        // let sliderConfig = {
        //     // type: "loop",
        //     fixedWidth: 300,
        //     height: 230,
        //     gap: 30,
        //     cover: true,
        //     pagination: false,
        //     lazyLoad: true,
        //     autoplay: true,
        //     rewind: true,
        //     perPage: 1,
        //     perMove: 1,
        //     focus: "start",
        //     breakpoints: {
        //         991: {
        //             fixedWidth: 260,
        //             height: 187,
        //         },
        //     },
        // };
        const nav = document.querySelector(".dash-main-slider__nav");
        let sliderConfig = {
            // type: "loop",
            fixedWidth: 300,
            height: 230,
            gap: 30,
            cover: true,
            pagination: true,
            lazyLoad: false,
            autoplay: true,
            arrows:{prev: nav.querySelector(".splide__arrow--prev"),next:nav.querySelector(".splide__arrow--next") },
            perPage: 3,
            perMove: 1,
            // arrows: false,
            rewind: true,
            breakpoints: {
                991: {
                    fixedWidth: 260,
                    height: 187,
                },
            },
        };

        /**
         * Slider
         */
        const slider = new Splide("#sliderDash", sliderConfig).mount();

        /**
         * Other Dashboard Sliders
         */
        const sliderDash3 = document.querySelectorAll(".cat-section-slider");
        // const sliderDash4 = document.querySelector("#sliderDash4");

        if (sliderDash3) {

            // const slider3 = new Splide(".cat-section-slider", sliderConfig).mount();
            sliderDash3.forEach(section_slider => new Splide(section_slider,sliderConfig).mount());
            // const slider4 = new Splide("#sliderDash4", sliderConfig).mount();

        }

    }
});
