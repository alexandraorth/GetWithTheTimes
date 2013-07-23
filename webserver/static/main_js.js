var section = "all-sections"

// beginning of function to change sections
function changeSection(name){
	section = name;
	console.log("from within changeSection, this is the section: " + section)
	renderImages();
}

// beginning of script to render images

function renderImages(){
	console.log("from within renderImages, this is the section " + section)
	var data; // a global
	var imgUrl = []; // a global
	var title = []; // a global
	var articleUrl = [];

	$.ajax({
		type: "get",
		url: "/queryArticles/<" + section + ">", 
		success: function(response) {
			data = JSON.parse(response);

			//go through response and populate arrays with information
			for (var i = 0; i < data.results.length; i=i+1) {
				if (data.results[i].type === "Article" && data["results"][i]["media"].length >= 1){ 

					if (data["results"][i]["media"][0]["media-metadata"] >= 5){
						imgUrl.push(data["results"][i]["media"][0]["media-metadata"][5]["url"]); 
						title.push(data["results"][i]["title"]);
						articleUrl.push(data["results"][i]["url"]);
					}

					else if (data["results"][i]["media"].length > 1 &&
						data["results"][i]["media"][1]["media-metadata"].length >= 5){
						imgUrl.push(data["results"][i]["media"][1]["media-metadata"][5]["url"]); 
						title.push(data["results"][i]["title"]);
						articleUrl.push(data["results"][i]["url"]);
					}	

					else if(section != "all-sections" 
						&& data["results"][i]["media"][0]["media-metadata"].length < 5
						&& data["results"][i]["media"][0]["media-metadata"].length >= 1){

						var holder = data["results"][i]["media"][0]["media-metadata"][0]["url"] 
						holder = holder.replace("thumbStandard", "square320")

						imgUrl.push(holder); 
						title.push(data["results"][i]["title"]);
						articleUrl.push(data["results"][i]["url"]);

					}
				}
			};	

			//go through populated arrays and place images on page
			for (var j = 0; j<imgUrl.length; j=j+1) {
				d3.select(".article" + (j+1))
				.attr("src", imgUrl[j])
				.attr("alt", title[j]);

				d3.select(".link" + (j+1))
				.attr("href", function(d){
					return "/compare/<" + articleUrl[j] + ">"
				})
				.on("click", function(d) { 
					console.log("look, ma " + this.getAttribute("href")); 

				});		
			}
		}
	});
}