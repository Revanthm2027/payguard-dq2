```python
  20 | app = FastAPI(
  21 |     title="PayGuard DQ API",
  22 |     middleware=[
  23 |         CORSMiddleware(
  24 |             allow_origins=["http://localhost:3000", "https://example.com"],  # replace with allowed origins
  25 |             allow_credentials=True,
  26 |             allow_methods=["*"],
  27 |             allow_headers=["*"],
  28 |         ),
  29 |     ],
```
    description="GenAI Agent for Universal, Dimension-Based Data Quality Scoring in Payments",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ingest.router)
app.include_router(runs.router)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "service": "Data Quality Scoring API",
        "status": "healthy",
        "version": "1.0.0"
    }


@app.get("/health")
async def health():
    """Health check."""
    return {"status": "ok"}
