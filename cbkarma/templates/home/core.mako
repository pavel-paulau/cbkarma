<%namespace name="dochead"  file="/common/dochead.mako"/>
<%namespace name="footer"   file="/common/footer.mako"/>

${dochead.html("cbkarma")}
<center>
    <div class="summary" id="summary-table">
        <p class="title">Dashboard</p>

        <table class="display" id="stats_table">
            <thead>
                <tr>
                    <th width="13%" class="left">Latest update</th>
                    <th width="14%" class="left">Spec. name</th>
                    <th width="10%" class="left">Build</th>
                    <th width="14%" class="left">Status</th>
                    <th width="35%" class="left">Description</th>
                    <th width="14%" class="left">Details</th>
                </tr>
            </thead>
            <tbody>
                % for row in range(len(data)):
                <tr>
                    <td class="left">${data[row]['timestamp']}</td>
                    <td class="left">${data[row]['spec']}</td>
                    <td class="left">${data[row]['build']}</td>
                    <td class="left">${data[row]['status']}</td>
                    <td class="left">${data[row]['description']}</td>
                    <td class="left">${data[row]['details']}</td>
                </tr>
                % endfor
            </tbody>
        </table>

    </div>
</center>
${footer.mako()}