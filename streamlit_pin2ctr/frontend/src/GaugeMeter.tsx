import React, { useEffect, useState } from "react"
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import GaugeChart from "react-gauge-chart"

/**
 * We can use a Typescript interface to destructure the arguments from Python
 * and validate the types of the input
 */
interface PythonArgs {
  label: string
  initialValue?: number
}

/**
 * No more props manipulation in the code.
 * We store props in state and pass value directly to underlying Slider
 * and then back to Streamlit.
 */
const GaugeMeter = (props: ComponentProps) => {
  // Destructure using Typescript interface
  // This ensures typing validation for received props from Python
  const { label, initialValue }: PythonArgs = props.args
  const [value, setValue] = useState(initialValue)
  const chartStyle = {
    height: 150,
  }

  useEffect(() => Streamlit.setFrameHeight())

  return (
    <>
      <h3>{label}</h3>
      <GaugeChart
        id="gauge-chart1"
        nrOfLevels={4}
        percent={value ? value / 100 : 0}
        colors={["#EA3323", "#F3AE3D", "#F8F826", "#75FB4C"]}
        needleColor="#D1CFCF"
        needleBaseColor="#D1CFCF"
        textColor="#464A4F"
      />
      <p>
        You're score is based on X, Y, and Z. Acaiberries gojiberries acroyoga{" "}
      </p>
    </>
  )
}

export default withStreamlitConnection(GaugeMeter)
