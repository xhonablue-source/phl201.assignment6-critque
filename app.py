```python
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Philosophical Critique | CognitiveCloud.ai",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and Author
st.title("Philosophical Critique")
st.subheader("Faulty Inference and Misleading Evidence versus Reliable Perception")
st.markdown("**By Xavier Honablue M.Ed**")
st.write("---")

# Full Essay Display
st.header("📜 Full Essay")
st.markdown("""
The Gettier problem challenges the classical definition of knowledge as justified true belief (JTB) 
by constructing cases in which a belief is true and justified but, intuitively, not knowledge. One of 
the most discussed examples is the “fake barn” scenario: a subject drives through an area filled with 
barn façades, happens to look at the one real barn, and forms the belief, “That is a barn.” According 
to the standard Gettier reading, the belief is true and justified but does not qualify as knowledge, 
because its truth is too dependent on environmental luck.

A critique of this reasoning centers on the role of perception. In the barn case, the subject’s 
perceptual faculties are functioning normally: she sees a barn, and there is in fact a barn. The 
justification is perceptual, not inferential. Unlike Gettier’s original cases, which rely on faulty 
inference or misleading evidence, the barn case involves accurate sensory experience directly 
connected to the truth of the belief. To call this “not knowledge” suggests that Gettier’s problem 
dismisses the reliability of perception as a basic source of justification.

This move places an implausibly high standard on knowledge. If knowledge requires immunity from all 
hidden environmental risks—such as the presence of fakes in the broader setting—then nearly all 
perceptual knowledge would be disqualified, since perception is always subject to unseen possibilities 
of error. A more reasonable view acknowledges that accurate perception provides knowledge when it 
correctly tracks reality, regardless of misleading conditions nearby. In the barn case, the subject 
knows she is looking at a barn precisely because her perception is both accurate and truth-conducive.

Thus, the barn scenario reveals a weakness in the Gettier framework: it treats knowledge as undermined 
even in cases where perception delivers truth directly. Far from exposing the insufficiency of JTB, 
the example shows that Gettier’s standard overlooks the central epistemic role of perception.
""")

st.write("---")

# Assignment Section
st.header("🎓 Classroom Assignment: Develop Your Own Critique")

st.markdown("""
Students will now write their own short philosophical critique using the structure modeled above.  
Your critique should be clear, structured, and argumentative.  
""")

# Suggested Structure
st.subheader("Suggested Structure")
st.markdown("""
1. **Introduction** – Briefly explain the problem, question, or scenario.  
2. **Case Example** – Present a concrete case or example to ground your discussion.  
3. **Critique / Analysis** – Identify what you think is missing, flawed, or overlooked in the reasoning.  
4. **Implications** – Explain why your critique matters. What does it change about how we think about the issue?  
5. **Conclusion** – Summarize your position clearly in 2–3 sentences.  
""")

# Sample Topics for Students
st.subheader("📚 Sample Topics to Critique")
st.markdown("""
Here are some philosophical ideas you could apply this critique structure to:

- **Plato’s Allegory of the Cave** – Does it overstate the unreliability of perception?  
- **Descartes’ Evil Demon / Cartesian Doubt** – Is radical doubt too skeptical to be useful?  
- **The Trolley Problem** – Does it simplify moral decision-making in unrealistic ways?  
- **Kant’s Categorical Imperative** – Can it handle complex, real-world ethical dilemmas?  
- **Nietzsche’s “God is Dead”** – What does this mean for morality, and is it too sweeping?  
- **Utilitarianism (Bentham/Mill)** – Does maximizing happiness ignore justice or rights?  
- **Gettier Problem (alternative cases)** – Do they really show JTB is insufficient?  
""")

# Footer
st.markdown("---")
st.markdown("Built by **Xavier Honablue M.Ed** for [CognitiveCloud.ai](https://cognitivecloud.ai)")
```
