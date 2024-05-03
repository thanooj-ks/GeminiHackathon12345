// set up text to print, each item in array is new line
var aText = new Array(
    "<p> Actionable Insights:<br> Areas for Improvement:<br> Staff Training: Addressing negative feedback regarding staff behavior is crucial. Training should focus<br> on customer service, respectful communication, and accurate information about fuel options and pricing.<br> Air Filling Service: Investing in reliable air filling equipment and training staff on its proper use is<br> essential to improve customer experience and safety.<br> Queue Management: Implementing strategies to improve queue management, particularly during peak hours,<br> would enhance customer satisfaction. Consider opening additional pumps or employing more staff during<br> busy periods.</p> <p> Improving Customer Experience:<br> Transparency: Ensure clear communication about fuel options and pricing to avoid misunderstandings and<br> accusations of dishonest tactics.<br> Feedback Mechanism: Establish a system for collecting and addressing customer feedback, demonstrating<br> responsiveness to concerns.</p> <p> Leveraging Positive Aspects: Marketing efforts can highlight the station's strengths, such as fuel<br> quality, 24/7 service, and positive customer experiences. Testimonials and positive reviews can be used<br> to build trust and attract customers.</p> <p> Additional Considerations:<br> Fake Reviews: While the provided data doesn't show clear signs of fake reviews, it's always recommended<br> to be vigilant for patterns or inconsistencies that might indicate inauthentic feedback.<br> Volume of Reviews: The analysis is based on a limited number of reviews and may not fully represent the<br> entire customer base.</p> <p> Recent Reviews: Focus on recent reviews as they reflect current customer experiences and the station's<br> current practices.</p>");
    var iSpeed = 10; // time delay of print out
    var iIndex = 0; // start printing array at this posision
    var iArrLength = aText[0].length; // the length of the text array
    var iScrollAt = 20; // start scrolling up at this many lines
     
    var iTextPos = 0; // initialise text position
    var sContents = ''; // initialise contents variable
    var iRow; // initialise current row
     
    function typewriter()
    {
     sContents =  ' ';
     iRow = Math.max(0, iIndex-iScrollAt);
     var destination = document.getElementById("typedtext");
     
     while ( iRow < iIndex ) {
      sContents += aText[iRow++] + '<br />';
     }
     destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "|";
     if ( iTextPos++ == iArrLength ) {
      iTextPos = 0;
      iIndex++;
      if ( iIndex != aText.length ) {
       iArrLength = aText[iIndex].length;
       setTimeout("typewriter()", 500);
      }
     } else {
      setTimeout("typewriter()", iSpeed);
     }
    }
    
    
    typewriter();