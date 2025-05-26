# Gemini Conversational Flow Design (SIIHA-Inspired)

## ✨ Purpose
This document outlines the initial design of a Gemini-based HR assistant conversational flow. It builds on the SIIHA framework and focuses on real-time, emotion-aware support for HR professionals and employees.

## 🎯 Objectives
- Detect and respond to emotional cues in workplace communication (e.g., shame, anxiety, frustration)
- Offer human-centered, trust-repairing rephrasings based on PHRI-aligned practices
- Prototype a contextual conversation agent using Gemini Studio design philosophy

## 🧠 Conversation Flow Sketch

1. **User Input** → Analyze for emotional cues using keyword & phrasing heuristics
2. **Emotion Detected** → Label emotion category (e.g., "anxiety", "shame")
3. **Response Strategy**:
   - Acknowledge emotion non-judgmentally
   - Offer trust-preserving reframe (e.g., alternative phrasing)
   - Optionally provide educational HR practice guidance (PHRI-aligned)

4. **User Choice**: Accept suggestion / Rephrase further / Ask HR procedural question
5. **Follow-up**: Save context if further interaction is needed

## 🔍 Example

**User:** I think I embarrassed myself in front of my manager. I shouldn't have spoken up.

**Bot:** It sounds like you're feeling a mix of regret and vulnerability. Thank you for sharing. Here's a possible way to reframe your message:

> "I spoke up because I care about the outcome. I welcome any feedback on how I expressed it."

Let me know if you'd like to practice how to say this or ask for HR support.

## 🧩 Suggested Modules to Implement
- `gemini_emotion_analyzer.py`
- `gemini_response_generator.py`
- `gemini_context_manager.py`

---
This flow is part of the Gemini-Aware branch development of the SIIHA Prototype.