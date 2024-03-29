<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
<a href="/"><pre>Back to Dashboard</pre></a>

<div id="tabs">
    <ul>
        <li><a href="#tabs-1">Summary</a></li>
        <li><a href="#tabs-2">Phases</a></li>
        <li><a href="#tabs-3">Histograms</a></li>
        <li><a href="#tabs-4">PDF Reports</a></li>
	</ul>
    <div id="tabs-1">
        <pre>build: <a href="http://builds.hq.northscale.net/latestbuilds/CHANGES_couchbase-server-${build}.txt">${build}</a></pre>
        <pre>specification: <a href="https://raw.github.com/couchbase/testrunner/master/conf/perf/${spec}.conf">${spec}</a></pre>
    </div>
    <div id="tabs-2">
        % for phase in phases:
            <pre>${phase}</pre>
        % endfor
    </div>
    <div id="tabs-3">
        % for description, attachment in histograms.items():
            <p><b>${description}</b></p>
            <pre>${attachment}</pre>
        % endfor
    </div>
    <div id="tabs-4">
        % if reports:
            <p><strong>Existing:</strong></p>
            <ul>
                % for description, url in reports.items():
                    <li><pre><a href="${url}" target="_blank">${description}</a></pre></li>
                % endfor
            </ul>
        % endif
        <p><strong>Add new:</strong></p>
        <form name="report" method="POST" action="/report">
            <pre>Description: <input type="text" name="description" /> URL:<input type="text" name="url" /> <input type="submit" name="submit" value="Submit" /></pre>
            <input type="hidden" name="test_id" value="${test_id}">
        </form>
    </div>
</div>
${footer.mako()}