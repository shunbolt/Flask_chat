$(document).ready(function()
{
	$("#min_max_button").click(function()
	{
		if($("i", this).attr('class').split(/\s+/)[1] == "fa-window-minimize")
      	{
       		$("i", this).toggleClass("fa-window-minimize", false).toggleClass("fa-window-maximize");
      	}
      	else
      	{
      		$("i", this).toggleClass("fa-window-maximize", false).toggleClass("fa-window-minimize");
      	}
       	$("#box").slideToggle();
    });
});