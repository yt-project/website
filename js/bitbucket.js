// we will add our javascript code here
 function format_commit(commit, reponame) {
    var url = "http://hg.enzotools.org/" + reponame + "/changeset/"
        + commit['node'];
    var user = commit['user'];
    var entry = "<li><a class='hash_node' href='" + url + "'>" + commit['node'] + "</a> "
              + "by <a href='https://bitbucket.org/"
                + user['username'] + "'>"
                + user['first_name'] + " " + user['last_name'] + "</a>"
                + ": "
    + commit['description'].substring(0,50);
    if (commit['description'].length > 50) { entry += "..."; }
    entry += "</li>";
    return entry;
 }
 function format_issue(issue, reponame) {
    var url = "http://hg.enzotools.org/" + reponame + "/issue/"
            + issue['local_id'];
    // Should put some kind of coloring based on severity here
    var entry = "<li><a class='issue_node' href='" + url + "'>"
              + "#" + issue['local_id'] + "</a>: "
              + issue['title'].substring(0, 80);
    if (issue['title'].length > 80) { entry += "..."; }
    entry += "</li>";
    return entry;
 }
 function populate_events(reponame) {
        function rv(bbdata) {
        var entry;
        var commits = $("#" + reponame + "_commits");
        $.each(bbdata['events'], function(intIndex, objValue) {
                if (objValue['event'] == "commit") {
                    entry = format_commit(objValue, reponame);
                    commits.append($(entry));
                }
            }
        );
    }; return rv;}
 function populate_issues(reponame) {
        function rv(bbdata) {
        var entry;
        var commits = $("#" + reponame + "_issues");
        $.each(bbdata['issues'], function(intIndex, objValue) {
                entry = format_issue(objValue, reponame);
                commits.append($(entry));
            }
        );
    }; return rv;}

 // INCOMING: http://hg.enzotools.org/yt/compare/USERNAME/yt..default
 // OUTGOING: http://hg.enzotools.org/yt/compare/default..USERNAME/yt
 function populate_forks(reponame) {
    function rv(fork_data) {
        var entry;
        var this_list = $("#" + reponame + "_forks");
        $.each(fork_data, function(intIndex, objValue) {
            if (objValue['reponame'] == undefined)
               {objValue['reponame'] = 'yt';}
            entry = "<li>"
                  + "<a href='http://hg.enzotools.org/yt/compare/"
                  + "default.." + objValue['username'] + "/"
                  + objValue['reponame'] + "'>"
                  + "<img src='img/box-icons/cogs.png' width=16 alt='Incoming Changesets'></a>"
                  + "&nbsp;&nbsp;"
                  + "<a href='https://bitbucket.org/"
                  + objValue['username'] + "/" + objValue['reponame'] + "/'>fork</a>"
                  + " by <a href='" + "https://bitbucket.org/"
                  + objValue['username'] + "'>"
                  + objValue['username'] + "</a>"
                  // incoming
                  //+ "<a href='http://hg.enzotools.org/yt/compare/"
                  //+ objValue['username'] + "/yt..default'>"
                  //+ "<img src='incoming.png' width=16></a>"
                  // outgoing
                  ;
            this_list.prepend($(entry));
        });
    };
    return rv;
}
