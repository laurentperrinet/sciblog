{%- extends 'slides_reveal.tpl' -%}

{% block input_group -%}
<div class="input_hidden">
{{ super() }}
</div>
{% endblock input_group %}

{% block prompt -%}
<div class="output_prompt">
{{ super() }}
</div>
{% endblock prompt %}

{%- block header -%}
{{ super() }}
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<style type="text/css">
.input_hidden {
  display: none;
}
.output_prompt {
  display: none;
}
table { 
   border : 0px
}
.reveal .slides section>* {
        margin-left: 0;
        margin-right: 0;
    }
</style>
{%- endblock header -%}

{% block body %}
{{ super() }}

<script>

Reveal.initialize({

    // The "normal" size of the presentation, aspect ratio will be preserved
    // when the presentation is scaled to fit different resolutions. Can be
    // specified using percentage units.
    width: 160%,
    height: 100%,

    // Factor of the display size that should remain empty around the content
    margin: 0.,

    // Bounds for smallest/largest possible scale to apply to content
    // minScale: 0.2,
    // maxScale: 1.5

    // Display controls in the bottom right corner
    controls: false,

    // Display a presentation progress bar
    progress: true,

    // Push each slide change to the browser history
    //history: false,

    // Vertical centering of slides
    center: true,

    // Enables touch navigation on devices with touch input
    touch: true,

    // Enable keyboard shortcuts for navigation
    //keyboard: true,

    // Enable the slide overview mode
    overview: true,

    // Loop the presentation
    //loop: false,

    // Change the presentation direction to be RTL
    //rtl: false,

    // Number of milliseconds between automatically proceeding to the
    // next slide, disabled when set to 0, this value can be overwritten
    // by using a data-autoslide attribute on your slides
    //autoSlide: 0,

    // Enable slide navigation via mouse wheel
    //mouseWheel: false,

    // Parallax background image
    // parallaxBackgroundImage: 'https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg', // e.g. "https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg"

    // Parallax background size
    // parallaxBackgroundSize: '2100px 900px', // CSS syntax, e.g. "2100px 900px" - currently only pixels are supported (don't use % or auto)

    // This slide transition gives best results:
    transition: 'fade', // default/cube/page/concave/zoom/linear/fade/none

    // Transition speed
    transitionSpeed: 'slow', // default/fast/slow

    // Transition style for full page backgrounds
    backgroundTransition: 'fade', // default/linear/none

    // Theme
    theme: 'White', // available themes are in /css/theme

});

</script>

{% endblock body %}