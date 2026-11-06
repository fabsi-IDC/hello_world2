import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";
import { MethodButton } from "../components/MethodButton";

const Timeservice: React.FC = () => {
  return (
    <div id="page-timeservice-1" style={{"background": "#2563eb", "--chart-color-palette": "default"}}>
    <div id="ih1wo" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="ih9e4" style={{
          "width": "250px",
          "padding": "20px",
          "display": "flex",
          "overflowY": "auto",
          "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)",
          "color": "white",
          "--chart-color-palette": "default",
          "flexDirection": "column"
        }}>
        <h2 id="ii32i" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="inx3k" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="igejr" style={{
              "padding": "10px 15px",
              "textDecoration": "none",
              "marginBottom": "5px",
              "display": "block",
              "background": "transparent",
              "color": "white",
              "borderRadius": "4px",
              "--chart-color-palette": "default"
            }} href="/helloworld">{"HelloWorld"}</a>
          <a id="imhov" style={{
              "padding": "10px 15px",
              "textDecoration": "none",
              "marginBottom": "5px",
              "display": "block",
              "background": "rgba(255,255,255,0.2)",
              "color": "white",
              "borderRadius": "4px",
              "--chart-color-palette": "default"
            }} href="/timeservice">{"TimeService"}</a>
        </div>
        <p id="i39lf" style={{
            "fontSize": "11px",
            "paddingTop": "20px",
            "marginTop": "auto",
            "textAlign": "center",
            "opacity": "0.8",
            "borderTop": "1px solid rgba(255,255,255,0.2)",
            "--chart-color-palette": "default"
          }}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="ihd8x" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="icgh9" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"TimeService"}</h1>
        <p id="i1x0f" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage TimeService data"}</p>
        <TableBlock id="table-timeservice-1" className="has-data-binding" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="TimeService List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true}} dataBinding={{"entity": "TimeService", "endpoint": "/timeservice/", "row_key_fields": ["id"]}} />
        <div id="i5mr3" style={{"marginTop": "20px", "display": "flex", "--chart-color-palette": "default", "flexWrap": "wrap", "gap": "10px"}}>
          <MethodButton id="icy2k" className="action-button-component" style={{
              "padding": "6px 14px",
              "fontSize": "13px",
              "fontWeight": "600",
              "textDecoration": "none",
              "letterSpacing": "0.01em",
              "display": "flex",
              "cursor": "pointer",
              "transition": "background 0.2s",
              "background": "linear-gradient(90deg, #2563eb 0%, #1e40af 100%)",
              "color": "#fff",
              "borderRadius": "4px",
              "border": "none",
              "boxShadow": "0 1px 4px rgba(37,99,235,0.10)",
              "--chart-color-palette": "default",
              "alignItems": "center"
            }} endpoint="/timeservice/{timeservice_id}/methods/getCurrentTime/" label="+ getCurrentTime" isInstanceMethod={true} instanceSourceTableId="table-timeservice-1" />
        </div>
      </main>
    </div>    </div>
  );
};

export default Timeservice;
