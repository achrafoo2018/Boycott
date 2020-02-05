document.getElementById("id_content").addEventListener("input", function () {
      	var lng = this.value.length;
      	document.getElementById("charcount").innerHTML = lng + ' / 30';});

// Checking for words length cuz if user give a big word it'll not fit in the post container
document.getElementById("id_content").addEventListener("change", function(){
    var content = document.getElementById("id_content").value.split(" ");
    maxlen = 0;
    for (i=0; i<content.length; i++) {
      if (content[i].length>maxlen) {
        maxlen = content[i].length;
      }
    }
    if (maxlen > 60)
    {
      document.getElementById('errorMessage').innerHTML ="Invalid Input Try Again";
      document.getElementById("errorMessage").className = "alert alert-warning";
      document.getElementById("id_content").value = "";
    }
});
