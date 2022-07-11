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
  minValue?: number
  maxValue?: number
  initialValue?: number[]
}

/**
 * No more props manipulation in the code.
 * We store props in state and pass value directly to underlying Slider
 * and then back to Streamlit.
 */
const GaugeMeter = (props: ComponentProps) => {
  // Destructure using Typescript interface
  // This ensures typing validation for received props from Python
  const { label, minValue, maxValue, initialValue }: PythonArgs = props.args
  const [value, setValue] = useState(initialValue)

  useEffect(() => Streamlit.setFrameHeight())
  Streamlit.setComponentValue(50)

  return (
    <>
      <h3>HELLO</h3>
      <GaugeChart id="gauge-chart2" nrOfLevels={20} percent={0.86} />
    </>
  )
}

export default withStreamlitConnection(GaugeMeter)
