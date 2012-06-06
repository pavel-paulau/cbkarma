<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
<a href="/"><pre>Back to Dashboard</pre></a>

<div id="tabs">
    <ul>
        <li><a href="#tabs-1">Summary</a></li>
        <li><a href="#tabs-2">Phases</a></li>
        <li><a href="#tabs-3">Histograms</a></li>
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
</div>
${footer.mako()}