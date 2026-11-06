import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { TableProvider } from "./contexts/TableContext";
import Helloworld from "./pages/Helloworld";
import Timeservice from "./pages/Timeservice";

function App() {
  return (
    <TableProvider>
      <div className="app-container">
        <main className="app-main">
          <Routes>
            <Route path="/helloworld" element={<Helloworld />} />
            <Route path="/timeservice" element={<Timeservice />} />
            <Route path="/" element={<Navigate to="/helloworld" replace />} />
            <Route path="*" element={<Navigate to="/helloworld" replace />} />
          </Routes>
        </main>
      </div>
    </TableProvider>
  );
}
export default App;
