# Stage 1: Build Stage
FROM public.ecr.aws/lambda/python:3.9.2025.04.03.11 as builder


WORKDIR /app


COPY app.py ./

# Stage 2: Final Stage
FROM public.ecr.aws/lambda/python:3.9.2025.04.03.11


WORKDIR /app


COPY --from=builder /app /app


CMD ["app.lambda_handler"]
