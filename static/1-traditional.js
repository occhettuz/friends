window.addEventListener("load", function(){
  // LET'S SAY THAT WE HAVE A SIMPLE FLAT ARRAY
  var data = ["doge", "cate", "birb", "doggo", "moon moon", "awkward seal"];

  // DRAW THE HTML TABLE
  var perrow = 3, // 3 items per row
      html = "<table><tr>";

  // Loop through array and add table cells
  for (var i=0; i<data.length; i++) {
    html += "<td>" + data[i] + "</td>";
    // Break into next row
    var next = i+1;
    if (next%perrow==0 && next!=data.length) {
      html += "</tr><tr>";
    }
  }
  html += "</tr></table>";

  // ATTACH HTML TO CONTAINER
  document.getElementById("container").innerHTML = html;
});