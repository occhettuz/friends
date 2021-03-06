window.addEventListener("load", function(){
  // LET'S SAY THAT WE HAVE A SIMPLE FLAT ARRAY
  var data = ["marco", "occhetta", "1G", "15", "matteo", "colombo", "3A", "12"];

  // DRAW HTML TABLE
  var perrow = 4, // 3 items per row
      count = 0, // Flag for current cell
      table = document.createElement("table"),
      row = table.insertRow();

  for (var i of data) {
    var cell = row.insertCell();
    cell.innerHTML = i;

    // You can also attach a click listener if you want
    cell.addEventListener("click", function(){
      alert("FOO!");
    });

    // Break into next row
    count++;
    if (count%perrow==0) {
      row = table.insertRow();
    }
  }

  // ATTACH TABLE TO CONTAINER
  document.getElementById("container").appendChild(table);
});