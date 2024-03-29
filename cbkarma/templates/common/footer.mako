<%def name="mako()">
<div class="footer">
    <div class="hr"></div>
</div>
<script type='text/javascript' src='/static/scripts/jquery-1.7.min.js'></script>
<script type='text/javascript' src='/static/scripts/datatables/jquery.dataTables.min.js'></script>
<script type='text/javascript' src='/static/scripts/datatables/ColReorder.min.js'></script>
<script type='text/javascript' src='/static/scripts/jquery-ui-1.8.21.custom.min.js'></script>

<script type='text/javascript'>
    $(document).ready(function() {
        $('#stats_table').dataTable({
            "bJQueryUI": true,
            "sPaginationType": "full_numbers",
            "sDom": 'R<"H"lfr>t<"F"ip<',
            "bAutoWidth": false,
            "iDisplayLength": 25,
            "aaSorting": [[ 0, "desc" ]]
        });
 
        $('#summary-table').css('visibility', 'visible');
    });
</script>

<script>
    $(function() {
        $( "#tabs" ).tabs({ selected: 0});
    });
</script>

</body>
</html>
</%def>