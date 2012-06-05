<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
<div class="summary" id="summary-table">
    <p class="title">Phases</p>
    % for phase in phases:
        <p>${phase}</p>
    % endfor
</div>
${footer.mako()}