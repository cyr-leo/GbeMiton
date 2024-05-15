$(document).ready(function(){
                    $("#import-button").on('click', function () {
                                console.log('start')

                        var query =($('#youtube-link').val());
                        //$("#event").html(query);
                        console.log(query);
                        console.log('tt');
                        var html_str = "";
                        $.ajax({
                            type : "GET",
                            url  : "/subdown/gen/",
                            data : {
                                "url": query
                            }
                             ,

                            success : function(data)
                            {

                                const results = JSON.parse(data.results);
                                console.log(results);

                            },
                            error: function(XMLHttpRequest, textStatus, errorThrown) {
                                console.log("Status: " + textStatus); //alert("Error: " + errorThrown);
                            }
                        });
                    });
                });