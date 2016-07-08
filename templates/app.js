var app = angular.module("sampleApp", [])
	.controller("officeController", function($scope) {
		$scope.persons = [
			{"FirstName": "John", "LastName": "Doe", "Country": "USA"}
		,	{"FirstName": "John", "LastName": "Dalton", "Country": "UK"} ,
			{"FirstName": "Alice", "LastName": "lake", "Country": "France"},
			{"FirstName": "Eli", "LastName": "lake", "Country": "France"},
			{"FirstName": "Emile", "LastName": "lake", "Country": "France"},
			{"FirstName": "Jin", "LastName": "lake", "Country": "France"},
			{"FirstName": "Min", "LastName": "lake", "Country": "France"},
			{"FirstName": "Jem", "LastName": "lake", "Country": "France"}
			];


		$scope.book = [
			{"Name": "Little Prince", "Author": "Alice", "Score": "5"},
			{"Name": "Ethica_: floating_time ", "Author": "Elie", "Score": "5"},
			{"Name": "On the move", "Author": "Oliver", "Score": "5"},
			{"Name": "Hero", "Author": "Doe", "Score": "4"},
			{"Name": "Alice in wonderland", "Author":
				"Luise", "Score": "4.5"},

		];

	})
	.directive('blackCircles', function() {
		return {
			restrict: 'EA',
			replace: true,
			link: function(scope, elem, attrs) {
				try {
					var dataset = [],
					    i = 0;

				    var num = parseInt(scope.num);

					for(i=0; i<15; i++){
					    dataset.push(Math.round(Math.random()*100));
					}

					var sampleSVG = d3.select(elem[0])
					    .append("svg")
					    .attr("width", $(elem[0]).width())
					    .attr("height", 75);

					sampleSVG.selectAll("circle")
					    .data(dataset)
					    .enter().append("circle")
					    .style("stroke", "gray")
					    .style("fill", "steelblue")
					    .attr("r", 25)
					    .attr("cx", function(d, i){return (i+1)*80})
					    .attr("cy", 35);
				} catch (e) {
					console.log(e);
				}
			}
		};
	})
	.directive('blueCircles', function() {
		return {
			restrict: 'EA',
			replace: true,
			link: function(scope, elem, attrs) {
				try {
					var dataset = [],
						i = 0;

					var num = parseInt(scope.num);

					for(i=0; i<7; i++){
						dataset.push(Math.round(Math.random()*100));
					}

					var sampleSVG = d3.select(elem[0]) //elem[0]
						.append("svg")
						.attr("width", $(elem[0]).width()) //elem[0]
						.attr("height", 75);

					sampleSVG.selectAll("circle")
						.data(dataset)
						.enter().append("circle")
						.style("stroke", "gray")
						.style("fill", "black")
						.attr("r", 25)
						.attr("cx", function(d, i){return (i+1)*80})
						.attr("cy", 35);
				} catch (e) {
					console.log(e);
				}
			}
		};
	})
	.directive('pinkCircles', function() {
		return {
			restrict: 'EA',
			replace: true,
			link: function(scope, elem, attrs) {
				try {
					var dataset = [],
						i = 0;

					var num = parseInt(scope.num);

					for(i=0; i<7; i++){
						dataset.push(Math.round(Math.random()*100));
					}

					var sampleSVG = d3.select(elem[0]) //elem[0]
						.append("svg")
						.attr("width", $(elem[0]).width()) //elem[0]
						.attr("height", 75);

					sampleSVG.selectAll("circle")
						.data(dataset)
						.enter().append("circle")
						.style("stroke", "gray")
						.style("fill", "coral")
						.attr("r", function(d){ return d*0.2; })
						.attr("cx", function(d, i){return (i+1)*80})
						.attr("cy", 35);
				} catch (e) {
					console.log(e);
				}
			}
		};
	})
	.directive('skyCircles', function() {
		return {
			restrict: 'E',
			scope:  { data: '='
			},

			link: function(scope, elem, attrs) {
				try {

					scope.$watch('data',function(data)
					{
						var sampleSVG = d3.select(elem[0])
							.append("svg")
							//.attr("width", $(elem[0]).width())
							.attr("width",1000)
							.attr("height", 500);

						sampleSVG.selectAll("circle")
							.data(data)
							.enter().append("circle")
							.style("stroke", "coral")
							.style("fill", "#dc94d6")
							.attr("r", function(d,i){ return d.Score/80 })
							.attr("cx", function(d, i){return (i+1)*80})
							.attr("cy", 35);
							/*.append("text")
							.attr("dx", function(d, i){return (i+1)*80})
							.attr("dy", 35)
							.text(function(d) { return d.Score; })
							.attr("fill", "green");*/
					});

				} catch (e) {
					console.log(e);
				}
			}
		};
	})
.directive('redCircles', function() {
	return {
		restrict: 'EA',
		replace: true,
		link: function(scope, elem, attrs) {
			try {
				var dataset = [],
					i = 0;

				var num = parseInt(scope.num);
               /*
				for(i=0; i<7; i++){
					dataset.push(Math.round(Math.random()*80));
				}
				*/

				//ng-model=book.score;

				//console.log('dataset_client:_',ng-model );
				angular.forEach(scope.data, function (book, index) {
					svg.append('rect')
						.attr('height', 20)
						.attr('width', book.Score)
						.attr('x', 0)
						.attr('y', 20*index)
						.attr('fill','steelblue');
						//.attr('fill', item.color);
				})


				var sampleSVG = d3.select(elem[0]) //elem[0]
					.append("svg")
					.attr("width", $(elem[0]).width()) //elem[0]
					.attr("height", 75);
               /*
				sampleSVG.selectAll("circle")
					.data(dataset)
					.enter().append("circle")
					.style("stroke", "gray")
					.style("fill", "gray")
					.attr("r", 10)
					.attr("cx", function(d, i){return (i+1)*80})
					.attr("cy", 35);
                */
				sampleSVG.selectAll("rect")
					.data(dataset)
					.enter().append("rect")
					.style('width',function(d,i){ return(i+1)*50} )
					.style('height',function(d,i){ return(d)*10})
					.style('fill','steelblue');

				console.log(scope.data);


			} catch (e) {
				console.log(e);
			}
		}
	};
});
