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

  useEffect(() => Streamlit.setFrameHeight())

  return (
    <>
      <h2 style={{ paddingTop: "10%" }}>{label}</h2>
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
        You're score is based on X, Y, and Z. Acaiberries gojiberries acroyoga.
        Acaiberries gojiberries acroyoga activatedcharcoal, acunpuncture gaia
        radicalacceptance colloidalsilver newparadigm, short-grainbrownrice
        fluorescentlights withadashofcayennepepper.
      </p>
    </>
  )
}

export default withStreamlitConnection(GaugeMeter)
