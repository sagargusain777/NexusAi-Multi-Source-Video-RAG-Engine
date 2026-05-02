
from pydantic import BaseModel, Field, HttpUrl

class VideoRequest(BaseModel):
    """Request body for endpoints that only need a YouTube URL."""
    url: HttpUrl = Field(
        ...,
        description="Full YouTube video URL",
        examples=["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    )

class QueryRequest(BaseModel):
    """Request body for the Q&A endpoint."""

    url: HttpUrl = Field(
        ...,
        description="Full YouTube video URL",
        examples=["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
    )
    question: str = Field(
        ...,
        min_length=3,
        description="The question to ask about the video content",
        examples=["What are the main points discussed in this video?"],
    )

class TranscriptResponse(BaseModel):
    """Returned when the user fetches a transcript."""

    video_id: str = Field(..., description="The 11-character YouTube video ID")
    language: str = Field(..., description="Language code of the transcript, e.g. 'en'")
    transcript_text: str = Field(..., description="Full transcript joined as plain text")
    chunk_count: int = Field(..., description="Number of chunks the transcript was split into")


class VideoSummary(BaseModel):
    """Structured output from the LLM when summarizing a video."""

    summary: str = Field(
        ...,
        description="A concise 3-5 sentence summary of the entire video",
    )
    key_points: list[str] = Field(
        ...,
        description="List of the most important points covered in the video",
    )
    topics: list[str] = Field(
        ...,
        description="High-level topic labels for the video content",
    )


class QueryAnswer(BaseModel):
    """Structured output from the LLM when answering a question."""

    answer: str = Field(
        ...,
        description="A clear, detailed answer to the user's question based on the video",
    )
    relevant_quotes: list[str] = Field(
        default_factory=list,
        description="Direct quotes from the transcript that support the answer",
    )
    confidence: str = Field(
        ...,
        description="Confidence level of the answer: 'high', 'medium', or 'low'",
        examples=["high", "medium", "low"],
    )


class Topic(BaseModel):
    """A single topic extracted from the video."""

    name: str = Field(..., description="Short topic name")
    description: str = Field(..., description="Brief description of what is discussed")
    timestamps: list[str] = Field(
        default_factory=list,
        description="Approximate timestamps where this topic appears, e.g. ['0:00', '3:45']",
    )


class TopicExtraction(BaseModel):
    """Structured output from the LLM when extracting topics."""

    topics: list[Topic] = Field(
        ...,
        description="List of distinct topics covered in the video",
    )
