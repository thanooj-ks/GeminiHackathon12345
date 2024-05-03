am4core.ready(function () {

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end

    var chart = am4core.create("chartdiv", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

    series.accuracy = 4;
    series.step = 15;
    series.rotationThreshold = 0.9;
    series.maxCount = 200;
    series.minWordLength = 2;
    series.labels.template.tooltipText = "{word}: {value}";
    // series.fontFamily = "Courier New";
    series.maxFontSize = am4core.percent(40);

    // series.colors = new am4core.ColorSet();
    // series.colors.passOptions = {};

    // series.text = "love love love love love love love love great easy fun sturdy cute perfect happy happy happy  imaginative recommend recommend recommend love great easy fun sturdy cute perfect happy imaginative recommend love great easy fun sturdy cute perfect happy imaginative recommend love great easy fun sturdy cute happy imaginative recommend love great easy fun sturdy cute perfect happy imaginative recommend love great fun sturdy cute perfect happy imaginative recommend love great easy fun sturdy cute perfect happy imaginative recommend love great easy fun sturdy cute perfect happy imaginative recommend";
    series.text = "loved it, loved it, loved it, great, great, great, recommended, recommended, Thankyou, Thankyou, Thankyou, Thankyou, Awesome Quality, Awesome Quality, Awesome Quality  ";

});