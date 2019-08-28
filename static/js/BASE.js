function updateGit(project, mod) {
    var post_data = {
        "project": project,
        "mod": mod,
    };
    alert("Close this Info to update " + project + " " + mod + "!");

    $.ajax({
        url: '/updateGit/',
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            alert(data["result"])
        }
    })
    ;
}

function kwsRun() {
    var post_data = {
        "target_str": document.getElementById(target_str),
    };
    $.ajax({
        url: '/asr-kws/',
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            alert(data);
            document.getElementById("info_wks").innerHTML = data;
        }
    })
}