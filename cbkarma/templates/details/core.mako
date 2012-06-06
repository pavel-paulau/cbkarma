<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
<div class="summary" id="summary-table">
    <a href="/"><pre>Back to Dashboard</pre></a>

    <p class="title">Phases</p>
    % for phase in phases:
        <pre>${phase}</pre>
    % endfor
    <p class="title">Histograms</p>
    % for description, attachment in histograms.items():
        <p><b>${description}</b></p>
        <pre>${attachment}</pre>
    % endfor
</div>
${footer.mako()}