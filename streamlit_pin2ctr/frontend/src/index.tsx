import React from "react"
import ReactDOM from "react-dom"
// import CustomSlider from "./CustomSlider"
import GaugeMeter from "./GaugeMeter"

// Lots of import to define a Styletron engine and load the light theme of baseui
import { Client as Styletron } from "styletron-engine-atomic"
import { Provider as StyletronProvider } from "styletron-react"
import { ThemeProvider, LightTheme } from "baseui"

const engine = new Styletron()

ReactDOM.render(
  <React.StrictMode>
    <StyletronProvider value={engine}>
      <ThemeProvider theme={LightTheme}>
        <GaugeMeter />
      </ThemeProvider>
    </StyletronProvider>
  </React.StrictMode>,
  document.getElementById("root")
)
