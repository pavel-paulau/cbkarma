<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
    <a href="/"><pre>Back to Dashboard</pre></a>

<div id="tabs">
	<ul>
        <li><a href="#tabs-1">Phases</a></li>
		<li><a href="#tabs-2">Histograms</a></li>
	</ul>
	<div id="tabs-1">
		% for phase in phases:
            <pre>${phase}</pre>
        % endfor
	</div>
	<div id="tabs-2">
		% for description, attachment in histograms.items():
            <p><b>${description}</b></p>
            <pre>${attachment}</pre>
        % endfor
	</div>
</div>
${footer.mako()}